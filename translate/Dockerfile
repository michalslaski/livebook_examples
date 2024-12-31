# Use the official Livebook image from GitHub Container Registry
FROM ghcr.io/livebook-dev/livebook

# Copy the local apps folder to the container's apps directory
COPY apps /apps

# Set the environment variable to point Livebook to the apps directory
ENV LIVEBOOK_APPS_PATH="/apps"
ENV LIVEBOOK_APPS_PATH_WARMUP="manual"
ENV LIVEBOOK_SHUTDOWN_ENABLED="true"

# Cache apps setup at build time
RUN /app/bin/warmup_apps

ENV LIVEBOOK_IP="::"
EXPOSE 8080
EXPOSE 8081

CMD [ "/app/bin/server" ]