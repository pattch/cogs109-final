import csv, re, sys

pattern = re.compile('[\W_]+')
# infile = 'lyrics100.csv'
# outfile = 'lyrics100cleaned.csv'
userfile = 'microblogPCU/weibo_user.csv'
postfile = 'microblogPCU/user_post.csv'

if len(sys.argv) > 2:
    userfile = sys.argv[1]
    postfile = sys.argv[2]

outfile = postfile.split('.')
outfile = outfile[0] + 'cleaned.' + outfile[1]
print('Processing',userfile,'and',postfile)

# First, build up sets for Spam and Non-Spam Accounts
spammer,hammer = set(),set()
with open(userfile,'r',encoding='latin-1') as f:
    next(f)
    data = csv.reader(f,delimiter=',')
    for l in data:
        user_id = l[0]
        spam = l[-1]
        if spam and int(spam.strip()) == -1:
            spammer.add(user_id)
        else:
            hammer.add(user_id)

print('Spammers:',len(spammer),'Non-Spammers:',len(hammer))

# Next, concatenate each post with the appropriate label
with open(postfile,'r',encoding='latin-1') as f:
    next(f)
    posts = []
    for l in f:
        content_start = ','.join(l.split(',')[2:])
        content = (content_start[::-1].split(',',6)[-1])[::-1]
        user_id = (content_start[::-1].split(',')[5])[::-1]

        label = '0'
        if user_id in spammer:
            label = '1'
        elif not user_id in hammer:
            print('Id in neither set:',user_id,l)

        post = label + ':' + content
        posts.append(post)

print('Finished Processing. Writing to',outfile)
print(len(posts))
with open(outfile,'w',encoding='latin-1') as f:
    for p in posts:
        # print(l)
        f.write(p + '\n')
