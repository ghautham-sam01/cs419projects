#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <time.h>

// Name: Ghautham Sambabu
// netID: gs878
// RUID: 201003148
// your code for time() goes here

static time_t (*orig_time)(time_t *t) = NULL;

time_t time(time_t *t) {
    static int first_call = 1;
    time_t desired_time;

    // Load the og time() if not yet loaded
    if (!orig_time) {
        orig_time = (time_t (*)(time_t *))dlsym(RTLD_NEXT, "time");
    }

    if (first_call) {
        // Set desired_time to my birthday =)
        struct tm valid_time = {.tm_year = 122, .tm_mon = 10,.tm_mday = 22,.tm_hour = 10,  
            .tm_min = 27,.tm_sec = 0,.tm_isdst = -1  
        };
        desired_time = mktime(&valid_time);
        first_call = 0;
    } else {
        // Use the og time() for next few calls
        return orig_time(t);
    }

    if (t) {
        *t = desired_time;
    }

    return desired_time;
}