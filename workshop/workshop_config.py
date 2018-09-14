import os

workshop.title = 'Workshop Guide'

workshop.courses = [
  'getting-started'
]

user = os.environ.get('JUPYTERHUB_USER', 'developer')
user = os.environ.get('OPENSHIFT_USER', user)

password = os.environ.get('OPENSHIFT_PASSWORD', 'openshift')

workshop.context = {
  'OPENSHIFT_USER': user,
  'OPENSHIFT_PASSWORD': password,
}
