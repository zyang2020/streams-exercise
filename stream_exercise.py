

class StreamProcessor(object):
    """
    Write a stream processor class that does the following:
        1. You initialize an instance with a stream of digits
          (AKA: file-like object, instance of StringIO), and
          store it as an instance variable.

          eg: f = io.StringIO("234761640930110349378289194")
              my_stream_processor = MyStreamProcessor(f)

        2. You call a `process` method of my_stream_processor.

          This method:

            1. Reads two digits at a time from the beginning of the stream
            2. Converts the two digits into a number, and adds that number
               to a running total.
            3. Once this number reaches 200 or more, the method returns how
               many two digit numbers it had to add together to reach its
               total.
            4. If `process` reaches the end of the stream BEFORE it has
               reached a sum of 200, then it will return how many two
               digit numbers it found before reaching the end of the
               stream.
            5. The method will add AT MOST 10 of these two digit numbers
               together: if it reaches the 10th two digit number and the
               sum has not yet reached 200, then the method will stop and
               return 10.

    For example, given a stream yielding "234761640930110349378289194", the
    process method will:

            1. Read two digits at a time from the stream: "23", "47", "61", etc.
            2. Convert these digits into a number: 23, 47, 61, etc., and  make a
               running total of these numbers: 23 + 47 equals 70. 70 + 61 equals
               131, etc.
            3. For this particular stream, the running total will exceed 200 after
               5 such additions: the `process` method should return 5.

    You can see the `tests.py` file for more examples of expected outcomes.
    """

    def __init__(self, stream):
        self._stream = stream

    def process(self):
        """
        TODO: Implement the `process` method, as described above.

        :return: int
        """
        count = 0 # count how many two-digit numbers the process has processed.
        tot = 0 # the sum of all two-digit numbers

        while count < 10 and tot < 200:
            digits = self._stream.read(2)# only read two digits at a time.
            if len(digits) < 2:
                break # if no more two-digits number then stop the process.
            count += 1

            n = int(digits) # cast the input to a integer
            tot += n
            #print(f'--- n:{n} tot:{tot} count:{count}')
        return count
