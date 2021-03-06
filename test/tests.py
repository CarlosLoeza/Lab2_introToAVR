# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'This test will check no spots taken and all spots available.',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 1 } ],'expected': [('PORTC',0x04)],
    },

  
    {'description': 'This test will check if 1 spot taken and 3 spots available.',
    	'steps': [ {'inputs': [('PINA',0x01)], 'iterations': 1 } ], 'expected': [('PORTC',0x03)],
    	'steps': [ {'inputs': [('PINA',0x02)], 'iterations': 1 } ], 'expected': [('PORTC',0x03)],
    	'steps': [ {'inputs': [('PINA',0x04)], 'iterations': 1 } ], 'expected': [('PORTC',0x03)],
    	'steps': [ {'inputs': [('PINA',0x08)], 'iterations': 1 } ], 'expected': [('PORTC',0x03)],
   },


   {'description': 'This test will check if 2 spot taken and 2 spots available.',
   	'steps': [ {'inputs': [('PINA',0x03)], 'iterations': 1 } ], 'expected': [('PORTC',0x02)],
    	'steps': [ {'inputs': [('PINA',0x05)], 'iterations': 1 } ], 'expected': [('PORTC',0x02)],
   	'steps': [ {'inputs': [('PINA',0x06)], 'iterations': 1 } ], 'expected': [('PORTC',0x02)],
   	'steps': [ {'inputs': [('PINA',0x09)], 'iterations': 1 } ], 'expected': [('PORTC',0x02)],
   	'steps': [ {'inputs': [('PINA',0x0A)], 'iterations': 1 } ], 'expected': [('PORTC',0x02)],
   	'steps': [ {'inputs': [('PINA',0x0C)], 'iterations': 1 } ], 'expected': [('PORTC',0x02)],
   },

 
   {'description': 'This test will check if 3 spot taken and 1 spots available.',
        'steps': [ {'inputs': [('PINA',0x07)], 'iterations': 1 } ], 'expected': [('PORTC',0x01)],
        'steps': [ {'inputs': [('PINA',0x0B)], 'iterations': 1 } ], 'expected': [('PORTC',0x01)],
        'steps': [ {'inputs': [('PINA',0x0D)], 'iterations': 1 } ], 'expected': [('PORTC',0x01)],
        'steps': [ {'inputs': [('PINA',0x0E)], 'iterations': 1 } ], 'expected': [('PORTC',0x01)],
   },


   {'description': 'This test will check if 4 spot taken and 0 spots available and set P7 to 1.',
        'steps': [ {'inputs': [('PINA',0x0F)], 'iterations': 1 } ], 'expected': [('PORTC',0x80)],
   },



    #{'description': 'This test will run second.',
    #'steps': [
    #{'inputs': [('PINA', 0x0F)],'iterations': 1}, ], 
    #'expected': [('PORTC', 0x0F)], 
    #},
    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
watch = ['main::tmpA','PORTC']

