# execute a command
exec { 'killmenow':
    command => 'pkill -i killmenow',
    path    => '/bin:/usr/bin:/usr/sbin',
}
