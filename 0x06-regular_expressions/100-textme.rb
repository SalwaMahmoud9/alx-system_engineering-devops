#!/usr/bin/env ruby
# 0x06. Regular expression
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
