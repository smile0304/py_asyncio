#python为了将语意变得更加明确，就引入了async和awit关键字用于定义原声协程
#from collections import Awaitable
import types
# async  def downloader(url):
#     return "TT"
@types.coroutine
def downloader(url):
    yield "TT"

async def download_url(url):
    #do somethine
    html = await downloader(url)
    return html

if __name__ == "__main__":
    coro = download_url("http://www.baidu.com")
    coro.send(None)