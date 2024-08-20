import configparser
from datetime import UTC, datetime

config = configparser.ConfigParser()
config.read("config.toml")

sections_of_interest = (
    "run",
    "structure",
    "db.postgres",
)

env_lines = [
    "# This .env file was automatically generated.",
    "# Do not edit directly.",
    "# Make changes in config.toml instead.",
    f"# Last generated: {datetime.now(UTC).isoformat()}",
]

for section in config.sections():
    if section in sections_of_interest:
        env_lines.append(f"\n#{section}")
        for key, value in config.items(section):
            value = value.strip('"')
            env_lines.append(f"{key.upper()}={value}")

with open(".env", "w") as f:
    f.write("\n".join(env_lines))
    print("dotenv is generated")
