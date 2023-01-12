# iptables

## display network interfaces
```shell
ip -4 addr show scope global
```
## public interface
```shell
ip route show | grep default
```

## the firewall
Iptables is used to set up, maintain, and inspect the tables of IP packet filter rules in the Linux kernel. Several 
different tables may be defined. Each table contains a number of built-in chains and may also contain user-defined 
chains.

### chain
* list of **rules**, which can match set of **packets**
* each rule specifies what to do with a packet, the activity is called a **target**
* target may be a jump to another, user-defined chain in the **same table**
* has default policy like:
  * `iptables --policy INPUT DROP` which is a default target

### target
* criteria for both packet and target
* if the packet doesn't match a rule, then the next rule in **chain** is examined
* special, built-in values:
  * **ACCEPT** means let the packet through
  * **DROP** means don't let through
  * **QUEUE** send packet to the **userspace**
  * **RETURN** chain policy decides what to do with the packet

### tables
There are 3 independent tables (presence of each depends on modules turned on in kernel).

#### filter
* the default one if no `-t` used
* contains three chains:
  * `INPUT` (incoming packets, destined to local sockets)
  * `FORWARD` (routed packets)
  * `OUTPUT` (outgoing packets, locally generated)

#### nat
This table is consulted when a packet that creates a new connection is encountered. It consists of three, built-in 
chains:
* `PREROUTING` alters packets just after it comes
* `OUTPUT` for altering locally-generated packets before routing
* `POSTROUTING` for altering packets just before they go out

#### mangle
Used for specialized packet alteration. Since Kernel **2.4.18** it has five default chains:
* `PREROUTING` alter packet before routing
* `OUTPUT` altering locally-generated packets before routing
* `INPUT` for packets coming to the box itself
* `FORWARD` for altering packets being **routed to the box**
* `POSTROUTING` for altering packets as they go out

### options
The options that are recognized by iptables can be divided into several groups.

#### commands
Command specifies action to be performed on a chain. They are represented by the _short_ and _long_ names.
* `-L, --list <chain>` list all rules in the selected chain
  * use `-t` if need to check other tables than default **filter**
  * use `-n` to avoid DNS lookups
* `-A, --append <chain> <rule>` append one or more rules **to the end** of the selected chain
* `-D, --delete <chain> <rule>` remove the specification from chain
* `-D, --delete <chain> [rulenum]` remove by the rule ordinal number
* `-I, --insert <chain> [rulenum] <rule>` insert one or more rule into the chain using a dedicated ordinal, rules in 
the chain starts with **1**
* `-R, --replace <chain> [rulenum] <rule>` replace a rule in the given chain
* `-N, --new-chain <chain>` create new, user-defined chain
* `-X, --delete-chain <chain>` delete user-defined chain
  * chain must be empty and user-defined
  * if no arguments passed it will remove every non-builtin chain in the table
* `-P, --policy <chain> <target>` set the policy for the chain
  * only built-in chains can have policies
* `-E, --rename-chain <old-name> <new-name>` rename user-specified chain

#### parameters
Parameters are the **rule specification**. Use **!**, to invert the test.
* `-p, --protocol [!] <protocol>` protocol of the rule
  * may be **tcp**, **udp**, **icmp** or **all**
  * **all** is default when omitted
* `-s, --source [!] <address/mask>` source specification
  * `address` can be **hostname**, ip with mask or just the ip
  * do not use hostname to **avoid DNS lookups**
* `-d, --destination [!] <address/mask>` destination specification
* `-j, --target <target>` specifies the target of the rule (what to do)
* `-g, --go-to <chain>` processing should continue in a user-specified chain
* `-i, --in-interface [!] <name>` interface where packet was received
* `-o, --out-interface [!] <name>` interface where packet will be sent

### rule dissection
|program|table| command    | chain   |parameters|target|
|-------|-----|------------|---------|----------|------|
|`iptables`|`-t filter`| `-A`| `INPUT` | `-p tcp --dport 80` |`-j ACCEPT`|

## iptables flowchart
![img](https://stuffphilwrites.com/wp-content/uploads/2014/09/FW-IDS-iptables-Flowchart-v2019-04-30-1.png)
