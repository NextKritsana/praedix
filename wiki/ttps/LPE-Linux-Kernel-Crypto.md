# TTP: Memory Map Injection via AF_ALG

**Summary**: A technique used to corrupt read-only memory pages (Page Cache) by exploiting kernel-level crypto subsystems that incorrectly handle shared memory buffers.

**Severity**: High
**Tactics**: Privilege Escalation, Defense Evasion
**Sources**: `Clippings\Copy Fail CVE-2026-31431 Nine Years of Root Access Hidden in the Linux Kernel.md`
**Last updated**: 2026-05-02

---

## Technical Details
This TTP involves bypassing standard file system write protections by leveraging the kernel's internal memory management. When `splice()` moves data, it passes references to physical memory pages rather than copying the data. If those references end up in a writable buffer (due to a logic flaw in a kernel module like `AF_ALG`), the kernel can be tricked into writing to "read-only" memory.

### Container Escape Context
This is particularly dangerous because the **Page Cache is shared across the entire kernel**.
- A process in a **Docker Container** or **Kubernetes Pod** shares the kernel with the Host.
- Corrupting the Page Cache from within a container affects the Host and all other containers on that same node.
- This breaks the isolation boundary of containers that do not use hardware-level virtualization (like Kata or Firecracker).

## Detection
- Monitor for the `splice()` syscall being used in conjunction with `AF_ALG` sockets.
- Behavioral analysis of processes that attempt to use `AF_ALG` without a valid application requirement (e.g., typical web servers don't use it).

## Related pages
- [[CVE-2026-31431]]
- [[OWASP_A06_Vulnerable_Outdated_Components]]
