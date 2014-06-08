
LON_ENV="lon-env"
REQUIREMENTS_FILE="requirements.txt"
LON_REPO_URL="https://github.com/lonapp/server"

if [ $(which virtualenv > /dev/null) ]; then
    echo "Error: virtualenv is not installed. Run 'pip install virtualenv'."
else
    if [ ! -d "${LON_ENV}" ]; then
        eval "virtualenv --no-site-packages --distribute ${LON_ENV}"
    fi

    echo "Activating ${LON_ENV}"
    source ${LON_ENV}/bin/activate
    pip install -qr ${REQUIREMENTS_FILE}

    _green=''
    _reset=''

    function lon()
    {
        function lon_usage()
        {
            echo "Usage: lon <command>"
            echo ""
            echo "Commands:"
            echo "  serve   Serve the Lon application locally"
            echo "  shell   Runs a Python shell inside Flask application context."
            echo "  dbup    Upgrade db schema to match latest models."
            echo "  db      Perform database actions."
            echo "  exit    Leave the virtual environment."
            echo "  help    Show this message."
            echo ""
            echo "Report issues to ${LON_REPO_URL}/issues"
        }

        if [ $# -eq 0 ]; then
            lon_usage
            return
        fi

        opt=$1
        case "${opt}" in
            help)
                lon_usage
                ;;
            shell)
                python run.py shell
                ;;
            serve)
                echo "Starting Lon server. Press Ctrl-C to exit."
                python run.py
                ;;
            exit)
                deactivate
                ;;
            *)
                lon_usage
                ;;
        esac
    }

    if [ ! -d "migrations" ]; then
        lon db init
        lon db migrate
    fi

    echo "Entering Lon virtual environment. Run 'lon' for more information."
fi
