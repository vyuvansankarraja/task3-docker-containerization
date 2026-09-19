# Linux Server Administration & Nginx Reverse Proxy

## 1. Linux User and SSH Security

A dedicated non-root user should be created for server administration.

```bash
sudo adduser deploy
sudo usermod -aG sudo deploy
```

SSH key authentication should be configured instead of password-based login.

Recommended SSH settings:

```text
PasswordAuthentication no
PermitRootLogin no
PubkeyAuthentication yes
```

## 2. UFW Firewall

Allow only the required ports:

```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status
```

| Port | Purpose |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |

## 3. Nginx Reverse Proxy

Nginx forwards incoming requests to the Flask application running on port 5000.

```text
Client
   |
   v
Nginx :80/:443
   |
   v
Flask Application :5000
```

The Nginx configuration includes proxy headers and reverse proxy settings.

## 4. Performance and Protection

The Nginx configuration includes:

- gzip compression
- Cache-Control headers
- Request rate limiting
- Reverse proxy headers

## 5. SSL/TLS

For a production server, HTTPS should be enabled on port 443.

Let's Encrypt Certbot can be used:

```bash
sudo apt update
sudo apt install nginx certbot python3-certbot-nginx
sudo certbot --nginx
```

For sandbox testing, a self-signed certificate can also be used.

## 6. Service Verification

Useful commands:

```bash
sudo systemctl status nginx
sudo nginx -t
sudo ufw status
curl http://localhost/
```

The Nginx configuration should pass `nginx -t` before reloading the service.

## 7. Security Summary

- Non-root administration user
- SSH key authentication
- Password-based SSH disabled
- Root SSH login disabled
- UFW firewall enabled
- Only ports 22, 80 and 443 exposed
- Nginx used as a reverse proxy
- HTTPS recommended for production
- Rate limiting enabled