import mx

print("****** In mx_sample.py")

def function(args=None):
   print "###### In function() for target 'fun'"

_suite = mx.suite('sample')
mx.update_commands(_suite,{
  'fun' : [function]}
)
