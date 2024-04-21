# client configuration
class { 'ssh::client':
  storeconfigs_enabled => false,
  options => {
    'Host *' => {
      'User' => 'ubuntu',
      'HostName' => '100.25.142.173',
      'IdentityFile' => '~/.ssh/school',
      'PasswordAuthentication' => 'no',
    },
  },
}
