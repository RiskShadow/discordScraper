#chat https://discord.com/channels/226368006115033091/670161269352824833
#message chat-messages-844626887833419796
import scrape
import download
import multiprocessing

print('1- Scrape\n2- Download\n')
choice = input('Please Select Number: ')

if choice == '1':
    scrape.scrape(input('Chat Link: '), input('Message ID: '))
if choice == '2':
    f = open('url.txt', 'r').read().split('\n')
    n = round(len(f)/8.)
    output = [f[i:i + n] for i in range(0, len(f), n)]
    ints = []
    startInt = 0
    for d in output:
        ints.append(startInt)
        startInt = startInt + len(d)

    process1 = multiprocessing.Process(target=download.download, args=(output[0],ints[0]))
    process2 = multiprocessing.Process(target=download.download, args=(output[1],ints[1]))
    process3 = multiprocessing.Process(target=download.download, args=(output[2],ints[2]))
    process4 = multiprocessing.Process(target=download.download, args=(output[3],ints[3]))
    process5 = multiprocessing.Process(target=download.download, args=(output[4],ints[4]))
    process6 = multiprocessing.Process(target=download.download, args=(output[5],ints[5]))
    process7 = multiprocessing.Process(target=download.download, args=(output[6],ints[6]))
    process8 = multiprocessing.Process(target=download.download, args=(output[7],ints[7]))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()

    print('Download Complete')


