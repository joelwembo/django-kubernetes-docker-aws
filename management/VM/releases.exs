import Config

config :phxroad, Phxroad.Repo,
 load_from_system_env: true, # <--- added
 # url:                        <--- moved to Repo.init
 pool_size: 20

config :phxroad, PhxroadWeb.Endpoint,
 load_from_system_env: true, # <--- added
 # http:                       <--- moved to Endpoint.init
 # url:                        <--- moved to Endpoint.init
 # secret_key_base:            <--- moved to Endpoint.init
 cache_static_manifest: "priv/static/cache_manifest.json",
 server: true,
 code_reloader: false

config :logger, level: :info