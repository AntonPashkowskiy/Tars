#include <stdio.h>
#include <stdlib.h>
#include <sys/inotify.h>
#include <unistd.h>

#define EVENT_SIZE  ( sizeof (struct inotify_event) )
#define BUF_LEN     ( 1024 * ( EVENT_SIZE + 16 ) )

int stop_monitor_flag = 0;

void process_incoming_messages(int main_inotify_descriptor, GSList* watcher_descriptor_list);
void process_incoming_events(int main_inotify_descriptor, GSList* watcher_descriptor_list, char* events_buffer);
int is_stop_monitor_flag_setted();

int main()
{
    int main_inotify_descriptor;
    GSList* watcher_descriptor_list = NULL;
    int list_length;
    int watcher_descriptor;
    int index;
    char events_buffer[BUF_LEN];

    main_inotify_descriptor = inotify_init();

    if (main_inotify_descriptor < 0)
    {
        perror("Inotify initializing failed.");
    }

    while(1)
    {
        process_incoming_messages(main_inotify_descriptor, watcher_descriptor_list);
        process_incoming_events(main_inotify_descriptor, watcher_descriptor_list, events_buffer);

        if (is_stop_monitor_flag_setted())
        {
            break;
        }
    }
    list_length = g_slist_length(watcher_descriptor_list);

    for (index = 0; index < list_length; index ++)
    {
        watcher_descriptor = *((int*)g_slist_nth_data(watcher_descriptor_list, index));
        inotify_rm_watch(main_inotify_descriptor, watcher_descriptor);
    }
    close(main_inotify_descriptor);
    g_slist_free(watcher_descriptor_list);
    return 0;
}

void process_incoming_messages(int main_inotify_descriptor, GSList* watcher_descriptor_list)
{

}

void process_incoming_events(int main_inotify_descriptor, GSList* watcher_descriptor_list, char* events_buffer)
{

}

int is_stop_monitor_flag_setted()
{
    return stop_monitor_flag > 0 ? 1 : 0;
}
