#!/usr/bin/env ruby
require 'json'
require 'mechanize'
require 'fileutils'

def main
  check_argv!

  id = ARGV[0]
  get_samples_to_files(id)
end

def check_argv!
  return if 1 == ARGV.size

  warn "usage: ruby #{__FILE__} 0001"
  exit 1
end

def get_samples_to_files(id)
  samples = get_samples(id)

  dir = "#{__dir__}/#{id}"
  FileUtils.mkdir(dir) unless File.exist?(dir)

  samples.each do |sample|
    sample_to_file(id, dir, sample)
  end
end

def get_samples(id)
  samples = nil

  Mechanize.new do |agent|
    res = agent.get("https://judgedat.u-aizu.ac.jp/testcases/samples/#{id}")
    samples = JSON.parse(res.body)
  end
  samples
end

def sample_to_file(id, dir, sample)
  i = sample['serial']
  File.write("#{dir}/sample#{i}.in", sample['in'])
  File.write("#{dir}/sample#{i}.out", sample['out'])
end

main
