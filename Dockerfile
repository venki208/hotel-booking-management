FROM postgres:15

# Set environment variables
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydb

# Expose PostgreSQL port
EXPOSE 5432

# Default command to run the database
CMD ["postgres"]