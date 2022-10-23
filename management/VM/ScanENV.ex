import Config # Config module

config :phxroad, Phxroad.Repo,
 url: System.fetch_env!("DATABASE_URL"),
 pool_size: String.to_integer(System.get_env("POOL_SIZE") || "10")

config :phxroad, PhxroadWeb.Endpoint,

 secret_key_base: System.fetch_env!("SECRET_KEY_BASE"),
 server: true