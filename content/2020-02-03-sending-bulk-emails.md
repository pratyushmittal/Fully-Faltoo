date: 2020-02-03
layout: post
title: Sending bulk emails
status: draft

We send around 1lac emails a day. It is a tough task because it involves multiple things:

- Setting up a server
	- reverse DNS
	- checking IP in blocklist
- Installing postfix
- Setting up SPF and DKIM
- Setting up authentication and firewall
- Monitoring server IP
- Adopting best practices:
	- Unsubscribe links
	- Handling bounces
- Debugging in case of errors

Most guides cover only one of these topics. I will try to share the "edge cases" and important things that are often missed. I will also link to good guides for general things.

## Setting up a server

DigitalOcean covers the basic server setup. Immediately after spinning a new server, we should check it's reputation. See if it is blocked on  We also need to configure the server for reverse DNS and ch