require 'yaml'
require 'json'
require 'uri'
require 'mechanize'

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
  Mechanize.new do |agent|
    header = {
      'Content-Type' => 'application/json; charset=utf-8'
    }

    json_auth = JSON.generate(auth)
    agent.post('https://judgeapi.u-aizu.ac.jp/session', json_auth, header)

    json_answer = JSON.generate(post_data_for(id))
    agent.post('https://judgeapi.u-aizu.ac.jp/submissions', json_answer, header)
  end
end

def post_data_for(id)
  data = {}
  data['problemId']  = id
  data['language']   = 'C'
  data['sourceCode'] = load_code_for(id)
  data
end

def load_code_for(id)
  ext = '.c'.freeze
  File.binread("#{id}#{ext}")
end

main
