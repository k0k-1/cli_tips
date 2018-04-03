#!/usr/bin/env ruby

print "> "
cmd = gets.chomp
syscmd = system( "#{cmd}" )
print syscmd
