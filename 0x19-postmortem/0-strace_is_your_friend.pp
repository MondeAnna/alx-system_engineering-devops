# correct 500 error

execute {'corret-php':
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
