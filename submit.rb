require 'yaml'
require 'net/http'
require 'uri'

def main
  check_argv!

  id = ARGV[0]
  auth = load_auth
  post_aoj(id, auth)
end

def check_argv!
  return if 1 == ARGV.size

  warn "usage: ruby #{__FILE__} 0001"
  exit 1
end

def load_auth
  yaml_name = 'submit.auth.yaml'.freeze
  yaml_path = File.join(File.dirname(File.expand_path(__FILE__)),
                        yaml_name)
  YAML.load_file(yaml_path)
end

def post_aoj(id, auth)
  uri  = URI.parse('http://judge.u-aizu.ac.jp/onlinejudge/servlet/Submit')
  data = post_data_for(id, auth)
  res  = http_post(uri, data)
  warn res
end

def http_post(uri, data)
  res = Net::HTTP.post_form(uri, data)
  res.body
end

def post_data_for(id, auth)
  data = auth.clone
  data['problemNO']  = id
  data['language']   = 'C'
  data['sourceCode'] = load_code_for(id)
  data
end

def load_code_for(id)
  ext = '.c'.freeze
  File.binread("#{id}#{ext}")
end

main
