print("Hello Worldddd!")
print("Started by user admin
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /Users/aabioumaima/.jenkins/workspace/python-pipeline
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Checkout)
[Pipeline] git
The recommended git tool is: NONE
No credentials specified
Cloning the remote Git repository
Cloning repository https://github.com/aabioumaima/python-jenkins.git
 > git init /Users/aabioumaima/.jenkins/workspace/python-pipeline # timeout=10
Fetching upstream changes from https://github.com/aabioumaima/python-jenkins.git
 > git --version # timeout=10
 > git --version # 'git version 2.39.3 (Apple Git-146)'
 > git fetch --tags --force --progress -- https://github.com/aabioumaima/python-jenkins.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git config remote.origin.url https://github.com/aabioumaima/python-jenkins.git # timeout=10
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > git rev-parse refs/remotes/origin/master^{commit} # timeout=10
Checking out Revision 8319f7969ed78014850adace85ed99dabfb53a19 (refs/remotes/origin/master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 8319f7969ed78014850adace85ed99dabfb53a19 # timeout=10
 > git branch -a -v --no-abbrev # timeout=10
 > git checkout -b master 8319f7969ed78014850adace85ed99dabfb53a19 # timeout=10
Commit message: "fjn"
First time build. Skipping changelog.
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] sh
+ python3 script.py
Hello Worldddd!
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] slackSend
Slack Send Pipeline step running, values are - baseUrl: <empty>, teamDomain: jenkinsprojectgroupe, channel: #sending-notifications, color: good, botUser: false, tokenCredentialId: slack, notifyCommitters: false, iconEmoji: <empty>, username: <empty>, timestamp: <empty>
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS")
