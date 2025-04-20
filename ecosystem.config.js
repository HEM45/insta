module.exports = {
  apps: [
    {
      name: 'mrin-script',
      script: 'mrin.py',
      interpreter: 'python3',
            cron_restart: '*/10 * * * *', // Restart every 5 minutes
      autorestart: true,           // Auto-restart on crash or failure
      watch: false,
      max_memory_restart: '512M',  // Optional
    }
  ]
};
