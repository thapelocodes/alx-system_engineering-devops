# kills process killmenow using `exec` and `pkill`
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
