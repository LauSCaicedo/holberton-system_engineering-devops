# Using strace, find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet
# (instead of using Bash as you were previously doing).

exec {'Replace':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i 's/phpp/php/g' /var/www/html/wp-settings.php'
}
