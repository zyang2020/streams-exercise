import io

from stream_exercise import StreamProcessor

score = 0


value = "234761640930110349378289194"
expected = 5
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
score += success
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "03050403020309060707070708"
expected = 10
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
score += success
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "3"
expected = 0
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
score += success
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "2347"
expected = 2
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
score += success
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "23478"
expected = 2
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
score += success
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


print("\n\nScore: {} of 5".format(score))
