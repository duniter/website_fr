#!/usr/bin/env bash
# 
## @file : develop_server.sh
## @brief : Script used to easily manage "Pelican" webserver
## @links :
## - Repository : https://github.com/duniter/website_fr
## - Wiki : https://duniter.org/fr/wiki/ameliorer-le-site 
#

##
# This section should match your Makefile
##

PY=${PY:-python}
PELICAN=${PELICAN:-pelican}
PELICANOPTS=""
BASEDIR=$(pwd)
INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py

###
# Don't change stuff below here unless you are sure
###

SRV_PID=$BASEDIR/srv.pid
PELICAN_PID=$BASEDIR/pelican.pid

# Print message to user who needs help
function usage(){
  echo "usage: $0 (stop) (start) (restart) [port]"
  echo "This starts Pelican in debug and reload mode and then launches"
  echo "an HTTP server to help site development. It doesn't read"
  echo "your Pelican settings, so if you edit any paths in your Makefile"
  echo "you will need to edit your settings as well."
  exit 3
}

# Check if virtualenv is set before to start Pelican webserver
function check_venv(){
  if [[ -z "$VIRTUAL_ENV" ]]
  then
    printf "%s\n" "Don't forget to setup your virtualenv !" "See REAME for more informations =)"
    exit 1
  fi
}

# Checking if process is running
function alive() {
  kill -0 "$1" >/dev/null 2>&1
}

# Function used to stop HTTP server
function shut_down(){
  check_venv

  # Manage HTTP server
  PID=$(cat "$SRV_PID" 2>/dev/null) # Hides output to users with stderr redirect
  if [[ $? -eq 0 ]]; then
    if alive "$PID"; then
      echo "Stopping HTTP server"
      kill "$PID"
    else
      echo "Stale PID, deleting"
    fi
    rm "$SRV_PID"
  else
    echo "HTTP server PIDFile not found"
  fi

  # Manage Pelican process
  PID=$(cat "$PELICAN_PID" 2>/dev/null) # Hides output to users with stderr redirect
  if [[ $? -eq 0 ]]; then
    if alive "$PID"; then
      echo "Killing Pelican"
      echo "Your HTTP server is stopped !"
      kill "$PID"
    else
      echo "Stale PID, deleting"
    fi
    rm "$PELICAN_PID"
  else
    echo "Pelican PIDFile not found"
    echo "Check if your HTTP server is running !"
  fi
}

# Function used to start HTTP server
function start_up(){
  check_venv
  local port=$1
  echo "Starting up Pelican and HTTP server"
  shift
  $PELICAN --debug --autoreload -r "$INPUTDIR" -o "$OUTPUTDIR" -s "$CONFFILE" $PELICANOPTS &
  pelican_pid=$!
  echo $pelican_pid > "$PELICAN_PID"
  cd "$OUTPUTDIR"
  $PY -m pelican.server "$port" &
  srv_pid=$!
  echo $srv_pid > "$SRV_PID"
  cd "$BASEDIR"
  sleep 1
  if ! alive $pelican_pid ; then
    echo "Pelican didn't start. Is the Pelican package installed?"
    return 1
  elif ! alive $srv_pid ; then
    echo "The HTTP server didn't start. Is there another service using port < $port > ?"
    return 1
  fi
  echo 'Pelican and HTTP server processes now running in background.'
}

###
#  MAIN
###

# Checking arguments passed to script
[[ ($# -eq 0) || ($# -gt 2) ]] && usage

# Default port number
DEFAULT_PORT=8556

# If necessary, set a default port number
if [[ (($1 == "start") || ($1 == "restart")) && (-z $2) ]]
then
  printf "%s\n" "Don't forget to set a port number (default value : $DEFAULT_PORT)"
  printf "%s\n" "If you want to overwrite this value :" "* Don't forget to set port number (see usage)" "* Don't forget to edit pelicanconf.py file (SITEURL value)"
  exit 1
else
  port=$2
fi

# Parse arguments and execute program
if [[ $1 == "stop" ]]; then
  shut_down
elif [[ $1 == "restart" ]]; then
  shut_down
  start_up "$port"
elif [[ $1 == "start" ]]; then
  if ! start_up "$port"; then
    shut_down
  fi
else
  usage
fi
