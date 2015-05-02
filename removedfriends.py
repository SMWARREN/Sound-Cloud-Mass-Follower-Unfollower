__author__ = 'SWarren'
import soundcloud
import time


def main():
    client = soundcloud.Client(
        client_id='',
        client_secret='',
        username='',
        password=''
    )

    fileOut = open('out.txt','w+')

    FollowMe = grab_followers_id(client)
    print(len(FollowMe))
    print(FollowMe)

    IFollow = grab_following_id(client)
    print(len(IFollow))
    print(IFollow)
    removedfriends = (list(set(IFollow) - set(FollowMe)))
    addfriends = (list(set(FollowMe) - set(IFollow)))
    print(addfriends, file=fileOut)

    counter = 0
    for i in removedfriends:
        deleteStr = "/me/followings/"+str(i)
        print("DELETING::",deleteStr)
        client.delete(deleteStr)
        if (counter%50 == 0):
            time.sleep(10)
        counter += 1

    
def grab_followers_id(client):
    page_limit = 50
    tList = []
    followerscount = client.get('/me').followers_count
    page_off = -1
    # Get names of each follower
    print("FOLLOWERS:"+str(+followerscount))
    for i in range(int(followerscount / page_limit) + 1):
        followers = client.get('/me/followers', offset=page_off, limit = page_limit )


        for follower in followers:
            tList.append(follower.id)


        page_off += page_limit
        time.sleep(10)
    return tList


def grab_following_id(client):
    page_limit = 50
    tList = []
    followerscount = client.get('/me').followings_count
    page_off = -1
    # Get names of each follower
    print("FOLLOWERS:"+str(+followerscount))
    for i in range(int(followerscount / page_limit) + 1):

        followers = client.get('/me/followings', offset=page_off, limit = page_limit )


        for follower in followers:
            tList.append(follower.id)


        page_off += page_limit
        time.sleep(10)
    return tList



if __name__ == "__main__":
    main()
