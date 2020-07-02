export start_server="gunicorn -b :9999 --daemon --reload wechat.wsgi"
echo "--> $start_server"
`$start_server`
echo Done.
