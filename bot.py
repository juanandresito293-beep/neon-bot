# -*- coding: utf-8 -*-
import discord
from discord.ext import commands

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
            title="✨ ¡UN NUEVO MIEMBRO HA LLEGADO!",
            description=f"Bienvenido/a {member.mention} a **NEON-VAULT**.\n\n🚀 Eres el miembro número **{len(member.guild.members)}**.\n\nNo olvides leer las reglas y disfrutar de nuestros servicios.",
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
            description=f"**{member.name}** ha abandonado la red.\nEsperamos volver a verte pronto.",
            color=0xff0000
        )
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
            
        embed.set_image(url=LINK_GIF)
        await canal.send(embed=embed)

# --- COMANDOS DE PRUEBA ---
@bot.command()
async def test_bienvenida(ctx):
    await ctx.message.delete()
    await on_member_join(ctx.author)

@bot.command()
async def test_despedida(ctx):
    await ctx.message.delete()
    await on_member_remove(ctx.author)

# --- COMANDO REGLAS ---
@bot.command()
async def reglas(ctx):
    await ctx.message.delete()
    texto = (
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "📜 **REGLAMENTO OFICIAL | NEON-VAULT**\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
        "🚫 **PROHIBICIONES ESTATUTARIAS**\n"
        "• **Spam & Flood:** Prohibido el envío masivo.\n"
        "• **Toxicidad:** Cero tolerancia al acoso.\n\n"
        "💳 **POLÍTICAS DE COMPRA**\n"
        "• **Garantía:** Soporte técnico de 24 a 48 horas.\n"
        "• **No Reembolsos:** Al ser productos digitales.\n\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "**Cualquier infracción resultará en BANEO PERMANENTE.** 🔨"
    )
    await ctx.send(embed=discord.Embed(description=texto, color=0xff0000))

# --- COMANDO MÉTODOS ---
@bot.command()
async def metodos(ctx):
    await ctx.message.delete()
    texto = (
        "💡 **INFORMACIÓN SOBRE NUESTROS MÉTODOS**\n\n"
        "Estrategias exclusivas y guías paso a paso.\n\n"
        "✅ **Probados** | 🚀 **Rápidos** | 🛡️ **Seguros**\n\n"
        "🛒 **¿QUIERES COMPRAR?**\n"
        "Abre un ticket aquí: <#1457597657076731904>"
    )
    await ctx.send(embed=discord.Embed(description=texto, color=0x00ffff))

# --- COMANDO PRÓXIMAMENTE ---
@bot.command()
async def proximamente(ctx):
    await ctx.message.delete()
    texto = (
        "🚀 **PRÓXIMAS ACTUALIZACIONES**\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
        "🛠️ **EN DESARROLLO:**\n"
        "• Nuevas Plantillas Web.\n"
        "• Scripts de Automatización.\n"
        "• Guías de Seguridad.\n\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    )
    await ctx.send(embed=discord.Embed(description=texto, color=0xffff00