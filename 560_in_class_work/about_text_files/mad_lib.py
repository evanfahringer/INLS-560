# Mad lib example for functions.

def madlib(noun_1,verb_1,verb_2,adverb_1,verb_3,adverb_2,noun_2,adverb_3):
   '''Mad lib function'''
   story = f'''
First, you need to grab your trusty {noun_1} , which should be well-maintained and ready for action. Check the fuel and make sure everything is in working order. After that, {verb_1} the handle firmly, and with determination, {verb_2} the lawnmower across the yard. As you go, make sure to move {adverb_1} , ensuring that you cut each patch of grass evenly. If the grass is extra tall, you may need to {verb_3} more {adverb_2} to get through it all without leaving clumps behind. Don't forget to keep an eye out for any {noun_2} in the grass that might get in your way—those could cause some serious problems! Finally, after mowing every corner of your yard, step back, look at the even lines you've created, and admire your freshly mowed lawn {adverb_3} . Time to relax!
    '''
   return story

output_story = madlib ('lawnmower','grip','push','carefully','trim','quickly','rocks','proudly')
print(output_story)