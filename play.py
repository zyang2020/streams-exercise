import io

from stream_exercise import StreamProcessor

# Play around with this string, if you like, to test your stream processor
value = "234761640930110349378289194"

my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()
print(result)
