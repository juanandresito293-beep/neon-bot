# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import os  # Importante para leer el token de Railway

# Configuración de permisos (Intents)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# --- CONFIGURACIÓN DE TU SERVIDOR ---
ID_BIENVENIDA = 1457925028946509979
ID_DESPEDIDA = 1457925064702955683
LINK_GIF = "https://cdn.discordapp.com/attachments/1456817792060756155/1457844891118731296/standard_8.gif"

@bot.event
async def on_ready():
    print(f'✅ SISTEMA NEON-VAULT ONLINE: {bot.user}')

# --- EVENTO DE BIENVENIDA ---
@bot.event
async def on_member_join(member):
    canal = bot.get_channel(ID_BIENVENIDA)
    if canal:
        embed = discord.Embed(
            title="✨ ¡BIENVENIDO A NEON-VAULT!",
            description=f"Hola {member.mention}, disfruta de nuestros servicios.\n\n🚀 Eres el miembro número **{len(member.guild.members)}**.",
            color=0x00ffff
        )
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
        
        embed.set_image(url=LINK_GIF)
        embed.set_footer(text="Seguridad y Calidad en un solo lugar.")
        await canal.send(embed=embed)

# --- EVENTO DE DESPEDIDA ---
@bot.event
async def on_member_remove(member):
    canal = bot.get_channel(ID_DESPEDIDA)
    if canal:
        embed = discord.Embed(
            title="🚪 UN USUARIO HA SALIDO",
            description=f"**{member.name}** ha abandonado la red.",
            color=0xff0000
        )
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
            
        embed.set_image(url=LINK_GIF)
        await canal.send(embed=embed)

# --- COMANDOS ---
@bot.command()
async def test_bienvenida(ctx):
    await on_member_join(ctx.author)

@bot.command()
async def test_despedida(ctx):
    await on_member_remove(ctx.author)

@bot.command()
async def reglas(ctx):
    await ctx.send("📜 **REGLAS:** Sé respetuoso, no hagas spam y sigue las instrucciones de los canales.")

@bot.command()
async def metodos(ctx):
    await ctx.send("💡 **MÉTODOS:** Revisa el canal <#1457597657076731904> para ver los servicios disponibles.")

# --- EJECUCIÓN SEGURA ---
# Railway leerá el token de sus variables de entorno
token = os.getenv("DISCORD_TOKEN")
bot.run(token)