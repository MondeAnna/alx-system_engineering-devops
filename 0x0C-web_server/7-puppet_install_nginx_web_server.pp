# create nginx server
exec {'prep os':
    provider => shell,
    command  => 'sudo apt -y update && sudo apt -y upgrade',
    before   => Exec['install-nginx'],
}

exec {'install-nginx':
    provider => shell,
    command  => 'sudo apt -y install nginx',
    before   => Exec['create-landing'],
}

exec {'create-landing':
    provider => shell,
    command  => 'echo "Hello World!" > /var/www/html/index.nginx-debian.html',
    before   => Exec['create-error'],
}

exec {'create-error':
    provider => shell,
    command  => 'echo "Ceci n\'est pas une page" > /usr/share/nginx/html/custom_404.html',
    before   => Exec['create-redirects'],
}

exec {'create-redirects':
    provider => shell,
    command  => 'sed -i "s/server_name _;/server_name _;\n\n\trewrite ^\/redirect_me https:\/\/stackoverflow.com\/a\/6045497 permanent;\n\n\terror_page 404 \/custom_404.html;\n\n\tlocation = \/custom_404.html {\n\t\troot \/usr\/share\/nginx\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-available/default',
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
