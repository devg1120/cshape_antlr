which python3
PARAM="./_Driver-Listener.py ObjectEditor.cs "

if [ "$?" -eq 0 ]; then
    echo "python3 found"
    python3 ${PARAM}
else
    which python
    if [ "$?" -eq 0 ]; then
        echo "python found"
        python ${PARAM}
    else
        echo "python3/python not found"
    fi
fi
 
