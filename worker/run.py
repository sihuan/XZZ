import json
from zzcore import StdAns
from config import GLOTTOKEN

LANGS = {
    'assembly': {'filename': 'main.assembly', 'url': 'https://run.glot.io/languages/assembly'}, 
    'ats': {'filename': 'main.ats', 'url': 'https://run.glot.io/languages/ats'}, 
    'bash': {'filename': 'main.bash', 'url': 'https://run.glot.io/languages/bash'}, 
    'c': {'filename': 'main.c', 'url': 'https://run.glot.io/languages/c'}, 
    'clojure': {'filename': 'main.clojure', 'url': 'https://run.glot.io/languages/clojure'}, 
    'cobol': {'filename': 'main.cobol', 'url': 'https://run.glot.io/languages/cobol'}, 
    'coffeescript': {'filename': 'main.coffeescript', 'url': 'https://run.glot.io/languages/coffeescript'}, 
    'cpp': {'filename': 'main.cpp', 'url': 'https://run.glot.io/languages/cpp'}, 
    'crystal': {'filename': 'main.crystal', 'url': 'https://run.glot.io/languages/crystal'}, 
    'csharp': {'filename': 'main.csharp', 'url': 'https://run.glot.io/languages/csharp'}, 
    'd': {'filename': 'main.d', 'url': 'https://run.glot.io/languages/d'}, 
    'elixir': {'filename': 'main.elixir', 'url': 'https://run.glot.io/languages/elixir'}, 
    'elm': {'filename': 'main.elm', 'url': 'https://run.glot.io/languages/elm'}, 
    'erlang': {'filename': 'main.erlang', 'url': 'https://run.glot.io/languages/erlang'}, 
    'fsharp': {'filename': 'main.fsharp', 'url': 'https://run.glot.io/languages/fsharp'}, 
    'go': {'filename': 'main.go', 'url': 'https://run.glot.io/languages/go'}, 
    'groovy': {'filename': 'main.groovy', 'url': 'https://run.glot.io/languages/groovy'}, 
    'haskell': {'filename': 'main.haskell', 'url': 'https://run.glot.io/languages/haskell'}, 
    'idris': {'filename': 'main.idris', 'url': 'https://run.glot.io/languages/idris'}, 
    'java': {'filename': 'main.java', 'url': 'https://run.glot.io/languages/java'}, 
    'javascript': {'filename': 'main.javascript', 'url': 'https://run.glot.io/languages/javascript'}, 
    'julia': {'filename': 'main.julia', 'url': 'https://run.glot.io/languages/julia'}, 
    'kotlin': {'filename': 'main.kotlin', 'url': 'https://run.glot.io/languages/kotlin'}, 
    'lua': {'filename': 'main.lua', 'url': 'https://run.glot.io/languages/lua'}, 
    'mercury': {'filename': 'main.mercury', 'url': 'https://run.glot.io/languages/mercury'}, 
    'nim': {'filename': 'main.nim', 'url': 'https://run.glot.io/languages/nim'}, 
    'ocaml': {'filename': 'main.ocaml', 'url': 'https://run.glot.io/languages/ocaml'}, 
    'perl': {'filename': 'main.perl', 'url': 'https://run.glot.io/languages/perl'}, 
    'perl6': {'filename': 'main.perl6', 'url': 'https://run.glot.io/languages/perl6'}, 
    'php': {'filename': 'main.php', 'url': 'https://run.glot.io/languages/php'}, 
    'python': {'filename': 'main.python', 'url': 'https://run.glot.io/languages/python'}, 
    'ruby': {'filename': 'main.ruby', 'url': 'https://run.glot.io/languages/ruby'}, 
    'rust': {'filename': 'main.rust', 'url': 'https://run.glot.io/languages/rust'}, 
    'scala': {'filename': 'main.scala', 'url': 'https://run.glot.io/languages/scala'}, 
    'swift': {'filename': 'main.swift', 'url': 'https://run.glot.io/languages/swift'}, 
    'typescript': {'filename': 'main.typescript', 'url': 'https://run.glot.io/languages/typescript'}
    }

class Ans(StdAns):

    def GETMSG(self):
        if len(self.parms) < 3:
            return '''Usage：
/run <lang>
<your code>
'''
        msg = f'{self.parms[0]}//{self.parms[1]}//{self.parms[2]}'
        return msg
