import mx

print("******In mx_sample.py")

def fun(args=None):
   print "###### In fun()"

_suite = mx.suite('sample')
mx.update_commands(_suite,{
  'fun' : [fun,'']}
)
