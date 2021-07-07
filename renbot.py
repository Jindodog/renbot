import discord
import os
import time
from discord.ext import commands, tasks
from playsound import playsound
from asyncio import sleep
from random import choice

bot = commands.Bot(command_prefix='@')

status = ['무한열차 시청', '역사 수업', '채점', '센쥬로 훈련 봐주기']

# 구동 알림
@bot.event
async def on_ready():
    change_status.start()
    print('[알림][煉獄 杏寿郎(우마이!)이 성공적으로 구동되었습니다.]')


# 봇끼리 대화
@bot.event
async def on_message(message):
    if message.content == "테스트":
        await message.channel.send("음! 안녕한가 카마도 소년!!")
        await bot.process_commands(message)
        return

    elif message.content == "🍠":
        #msg = await message.channel.send("🤤")
        #await msg.add_reaction("🤤")
        
        #await message.add_reaction(🤤)
        await message.channel.send("왓쇼이!!!!!")

    await bot.process_commands(message)
    return

@bot.command(name="따봉")
async def reaction(ctx):
    await ctx.message.add_reaction('👍')

# 대화
@bot.command()
async def 안녕(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client
        
    vc.play(discord.FFmpegPCMAudio('um.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="음! 반갑다! 나는 렌고쿠 쿄주로 라고 한다!!!")
    embed.set_image(url="https://2.gall-gif.com/tdgall/files/attach/images/82/665/576/094/14eaa908789d24e3b1cfb7be0d99b086.gif")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()


@bot.command()
async def 그열차타지마요(ctx):
    embed = discord.Embed(color=discord.Colour.red(), title="이것 또한 나의 사명!")
    embed.set_image(url="https://2.gall-gif.com/tdgall/files/attach/images/82/665/576/094/16ff46a8df566d595458e351d7ece6fc.gif")
    await ctx.message.channel.send(embed=embed)

@bot.command()
async def 이름일본어로(ctx):
    await ctx.channel.send('煉獄 杏寿郎!')

@bot.command()
async def 대사1(ctx):
    await ctx.channel.send('가슴을 펴고 살아가거라')

@bot.command()
async def 대사2(ctx):
    await ctx.channel.send('자신의 약함이나 변변치 못한 모습에 몇번이고 꺾이게 되어도 마음을 불태우며 이를 악물고 앞을 향하거라')

@bot.command()
async def 대사3(ctx):
    await ctx.channel.send('자네가 발을 멈추고 주저해도 시간의 흐름은 멈춰주지 않아. 함께 멈춰서서 슬퍼해주지 않는 것이야')

@bot.command()
async def 대사4(ctx):
    await ctx.channel.send('내가 여기서 죽는 것은 개의치 말거라. 지주라면 후배의 방패가 되어주는 건 당연한 일이니')

@bot.command()
async def 대사5(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('1.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="이런 이런")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.4)
    embed = discord.Embed(color=discord.Colour.red(), title="지주로서 부끄러울 따름이구나")
    await ctx.message.channel.send(embed=embed)
    await sleep(2.4)
    embed = discord.Embed(color=discord.Colour.red(), title="쥐구멍이 있다면")
    await ctx.message.channel.send(embed=embed)
    await sleep(2.2)
    embed = discord.Embed(color=discord.Colour.red(), title="들어가고 싶구나!")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 대사6(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('2.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="나이를 먹는 것도")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.2)
    embed = discord.Embed(color=discord.Colour.red(), title="죽는 것도")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.2)
    embed = discord.Embed(color=discord.Colour.red(), title="인간이라고 하는 덧없는 생명의 아름다움")
    await ctx.message.channel.send(embed=embed)
    await sleep(4.2)
    embed = discord.Embed(color=discord.Colour.red(), title="늙기 때문에")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.5)
    embed = discord.Embed(color=discord.Colour.red(), title="죽기 때문에")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.9)
    embed = discord.Embed(color=discord.Colour.red(), title="한없이 사랑스럽고")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.4)
    embed = discord.Embed(color=discord.Colour.red(), title="소중한 것이다")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 대사7(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('3.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="나는")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.5)
    embed = discord.Embed(color=discord.Colour.red(), title="나의 책무를 다 할 것이다!")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 대사8(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('4.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="여기 있는 자들은")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.1)
    embed = discord.Embed(color=discord.Colour.red(), title="그 누구도 죽게 하지 않겠다!")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
       #await sleep(1)
    #await vc.disconnect()


@bot.command()
async def 저기(ctx):
    await ctx.channel.send('우마이!')

@bot.command()
async def 아카자(ctx):
    await ctx.channel.send('난 벌써 그 자가 싫다!')

@bot.command()
async def 형님(ctx):
    await ctx.channel.send('제자로 받아주지!')

@bot.command()
async def 사랑해(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('ofcourse.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="그야 그럴 테지!")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.5)
    embed = discord.Embed(color=discord.Colour.red(), title="하하하하하하하!")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 센쥬로(ctx):
    await ctx.channel.send('자신이 마음가는대로 살아가거라')

@bot.command()
async def 고구마밥(ctx):    
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('um.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2
    
    embed = discord.Embed(color=discord.Colour.red(), title="음!")
    await ctx.message.channel.send(embed=embed)
    await sleep(1)
    embed = discord.Embed(color=discord.Colour.red(), title="내가 제일 좋아하는 음식이군!!")
    await ctx.message.channel.send(embed=embed)
    await sleep(1.5)

    vc.play(discord.FFmpegPCMAudio('umai.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="우마이!!")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 바보야(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('maybe.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="과연!")
    await ctx.message.channel.send(embed=embed)
    await sleep(1)
    embed = discord.Embed(color=discord.Colour.red(), title="난 바보인가!")
    embed.set_image(url="https://2.gall-gif.com/tdgall/files/attach/images/82/665/576/094/16ff46a8df566d595458e351d7ece6fc.gif")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 이럴수가(ctx):
    embed = discord.Embed(color=discord.Colour.red(), title="요모야 요모야다")
    embed.set_image(url="https://raw.githubusercontent.com/Jindodog/renbot/main/%EC%9A%94%EB%AA%A8%EC%95%BC.gif")
    await ctx.message.channel.send(embed=embed)

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('yomoya.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 부끄러워(ctx):
    file = discord.File("쥐구멍2.gif")
    embed = discord.Embed(color=discord.Colour.red(), title="쥐구멍이 있다면 들어가고 싶구나!")
    embed.set_image(url="attachment://쥐구멍2.gif")
    await ctx.send(embed=embed, file=file)

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('mouseholl.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 수박게임(ctx):
    await ctx.channel.send('https://daxigua-master-d4uma7rx4.vercel.app/')

@bot.command()
async def 어머니(ctx):
    await ctx.channel.send('어머니.. 저는 제 책무를 다한 걸까요?')

@bot.command()
async def 제1형(ctx):
    await ctx.channel.send('いちのかた しらぬい - 이치노카타 시라누이 / 제1형 부지화')

@bot.command()
async def 제2형(ctx):
    await ctx.channel.send('にのかた のぼりえんてん - 니노카타 노보리엔텐 / 제2형 상승염천')

@bot.command()
async def 제3형(ctx):
    await ctx.channel.send('さんのかた きえんばんしょう - 산노카타 키엔반쇼ㅡ / 제3형 기염만상')

@bot.command()
async def 제4형(ctx):
    await ctx.channel.send('しのかた せいえんのうねり - 시노카타 세ㅡ엔노우네리 / 제4형 성염의 파도')

@bot.command()
async def 제5형(ctx):
    await ctx.channel.send('ごのかた えんこ - 고노카타 엔코 / 제5형 염호')

@bot.command()
async def 오의(ctx):
    file = discord.File("연옥.gif")
    embed = discord.Embed(color=discord.Colour.red(), title="화염의 호흡 오의 제9형 연옥!", description="ほのおのこきゅう おうぎ くのかた・れんごく")
    embed.set_footer(text="호노오노 코큐ㅡ 오ㅡ기 쿠노카타 렌고쿠")
    embed.set_image(url="attachment://연옥.gif")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def 고소(ctx):
    await ctx.channel.send('감옥이 있다면 들어가고 싶구나!')

@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(color=discord.Colour.red(), title="렌고쿠 쿄주로 봇 도움말", description="접두사는 `@` 입니다.")
    embed.add_field(name="대화", value="`그열차타지마요`, `이름일본어로`, `대사1 ~ 4`, `저기`, `아카자`, `형님`, `센쥬로`, `수박게임`, `어머니`, `제1형 ~ 제5형`, `오의`, `고소`, `테스트`, `잘자`, `언급`, `포스터`", inline=False)
    embed.add_field(name="음성", value="`안녕`, `사랑해`, `바보야`, `고구마밥`, `이럴수가`, `부끄러워`, `우마이`, `대사5~8`, `아무말`, `악어죽이자`", inline=False)
    embed.add_field(name="제작자", value="`김진돌`", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 테스트(ctx):
    await ctx.channel.send('아주 잘 되는군!')

@bot.command()
async def 잘자(ctx):
    await ctx.channel.send(f'{ctx.author.mention}도 잘자게!')

@bot.command()
async def 언급(ctx):
    await ctx.channel.send(f'{ctx.author.mention}!!!!')

@bot.command()
async def 포스터(ctx):
    with open('1.png', 'rb') as fp:
        await ctx.channel.send(file=discord.File(fp, '1.png'))

@bot.command()
async def 우마이(ctx):
    embed = discord.Embed(color=discord.Colour.red(), title="우마이!")
    embed.set_image(url="https://2.gall-gif.com/tdgall/files/attach/images/82/665/576/094/e1b1478d0cd7c28b0db709f088742772.gif")
    await ctx.message.channel.send(embed=embed)

    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('umai.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 아무말(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('noidea.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="이해할 수 없는 생각이로군!")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 악어죽이자(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('onlywe.mp3'))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.2

    embed = discord.Embed(color=discord.Colour.red(), title="우리들만으로 처분 가능!")
    await ctx.message.channel.send(embed=embed)

    #while vc.is_playing():
        #await sleep(1)
    #await vc.disconnect()

@bot.command()
async def 렌고쿠생일축하해(ctx):
    embed = discord.Embed(color=discord.Colour.red(), title="음! 모두들 고맙군!!")
    await ctx.message.channel.send(embed=embed)
    embed = discord.Embed(color=discord.Colour.red(), title="기쁘다!!!")
    await ctx.message.channel.send(embed=embed)

@bot.command()
async def 들어와(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is None:
        vc = await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)
        vc = ctx.voice_client
        
        embed = discord.Embed(color=discord.Colour.red(), title="이미 들어와있다!!")
        await ctx.message.channel.send(embed=embed)


@bot.command()
async def 잘가(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return
    
    channel = ctx.message.author.voice.channel
    vc = ctx.voice_client
    
    if ctx.voice_client is None:
        embed = discord.Embed(color=discord.Colour.red(), title="난 거기에 없다만!!")
        await ctx.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(color=discord.Colour.red(), title="음! 즐거웠다!!")
        await ctx.message.channel.send(embed=embed)

        await vc.disconnect()


@bot.command()
async def 심한말(ctx):
    await ctx.channel.send('!!!')
    await ctx.channel.send('음..! 다소 거친 말을 하는군!!')
#

@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status)))

bot.run(os.environ['token'])
