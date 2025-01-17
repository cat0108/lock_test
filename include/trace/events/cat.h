#undef TRACE_SYSTEM
#define TRACE_SYSTEM cat

#if !defined(_TRACE_CAT_H) || defined(TRACE_HEADER_MULTI_READ)
#define _TRACE_CAT_H

#include <linux/tracepoint.h>
#include <linux/ktime.h>


TRACE_EVENT(folio_lock_timer,
    TP_PROTO(int cpu, unsigned long wait_time_ns),
    TP_ARGS(cpu, wait_time_ns),
    TP_STRUCT__entry(
        __field(int, cpu)
        __field(unsigned long, wait_time_ns)
    ),
    TP_fast_assign(
        __entry->cpu = cpu;
        __entry->wait_time_ns = wait_time_ns;
    ),
    TP_printk("cpu=%d, wait_time_ns=%lu", __entry->cpu, __entry->wait_time_ns)
);

#endif /* _TRACE_CAT_H */

/* This part must be outside protection */
#include <trace/define_trace.h>
