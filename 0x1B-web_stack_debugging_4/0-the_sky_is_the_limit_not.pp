#change ulimit for nginx server and prevent unfulfilled requests

exec {'update':
        #command => "sed -i 's/ULIMIT/ULIMITer/' /etc/default/nginx",
        command => "echo 'ULIMIT=\"-n 4096\"' > /etc/default/nginx",
        path => ['/usr/local/bin/', '/bin/'],
}

exec {'restartNginx':
        command => "service nginx restart",
        path => "/usr/bin/"
}
