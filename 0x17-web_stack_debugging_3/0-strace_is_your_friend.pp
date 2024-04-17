#use puppet to configure a server and save the configuration for future use
#this file is not an excutable program but a configuration file hence we use - puppet apply to apply the changes to our server

exec {'test':
        command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
        provider => 'shell'
}
