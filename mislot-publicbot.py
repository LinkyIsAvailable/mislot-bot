import disnake
from disnake.ext import commands
from tavily import TavilyClient

# List of authorized server IDs
AUTHORIZED_SERVERS = [
    12345,  # Replace by your actual server IDs
    12345
]

intents = disnake.Intents.default()
bot = commands.InteractionBot(intents=intents)

client = TavilyClient(api_key="your_tavily_api_key")

class CategorySelect(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Emploi", description="Rechercher des offres d'emploi", value="emploi"),
            disnake.SelectOption(label="Logement", description="Rechercher des logements", value="logement"),
            disnake.SelectOption(label="Formation", description="Rechercher des formations", value="formation"),
            disnake.SelectOption(label="Mobilité", description="Rechercher des services de mobilité", value="mobilite"),
            disnake.SelectOption(label="Santé", description="Rechercher des services de santé", value="sante")
        ]
        super().__init__(
            placeholder="Choisissez une catégorie",
            options=options,
            custom_id="category_select"
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        # Create a modal for the department input
        modal = DepartementModal(self.values[0])
        await interaction.response.send_modal(modal)

class DepartementModal(disnake.ui.Modal):
    def __init__(self, category):
        self.category = category
        components = [
            disnake.ui.TextInput(
                label="Département",
                placeholder="Entrez votre département",
                custom_id="departement",
                style=disnake.TextInputStyle.short,
                max_length=50
            ),
        ]
        super().__init__(title="Entrez votre département", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        departement = interaction.text_values["departement"]
        await interaction.response.defer()

        # Build the query based on the category
        queries = {
            "emploi": f"offres d'emploi en {departement}",
            "logement": f"offres de logement en {departement}",
            "formation": f"centres de formation en {departement}",
            "mobilite": f"services de transport en {departement}",
            "sante": f"services de santé en {departement}"
        }
        
        query = queries[self.category]
        response = client.search(query)

        if response and "results" in response and response["results"]:
            embed = disnake.Embed(
                title=f"🔍 Résultats {self.category} pour {departement}", 
                color=disnake.Color.blue()
            )

            for result in response["results"][:5]:
                title = result.get("title", "Titre non disponible")
                content = result.get("content", "Pas de description disponible")
                url = result.get("url", "URL indisponible")
                embed.add_field(name=title, value=f"{content}\n[🔗 Lien]({url})", inline=False)

            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"❌ Aucun résultat trouvé pour {self.category} en {departement}.")

class CategoryView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.add_item(CategorySelect())

@bot.slash_command(
    description="Rechercher des informations par catégorie et département",
    guild_ids=AUTHORIZED_SERVERS
)
async def requete(interaction: disnake.ApplicationCommandInteraction):
    # Check if the command is authorized on the server
    if interaction.guild_id not in AUTHORIZED_SERVERS:
        await interaction.response.send_message("❌ Cette commande n'est pas disponible sur ce serveur.", ephemeral=True)
        return
        
    view = CategoryView()
    await interaction.response.send_message("Veuillez choisir une catégorie :", view=view)

bot.run("your_token")
