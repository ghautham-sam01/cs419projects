#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dlfcn.h>
#include <dirent.h>

// Name: Ghautham Sambabu
// netID: gs878
// RUID: 201003148
// your code for readdir() goes here

struct dirent *readdir(DIR *dirp) {
    static void *handle = NULL;
    static struct dirent *(*orig_readdir)(DIR *) = NULL;

    if (!handle) {
        handle = dlopen("libc.so.6", RTLD_LAZY);
        if (!handle) {
            fprintf(stderr, "dlopen() failed: %s\n", dlerror());
            exit(1);
        }

        orig_readdir = dlsym(handle, "readdir");
        if (!orig_readdir) {
            fprintf(stderr, "dlsym() failed: %s\n", dlerror());
            exit(1);
        }
    }

    struct dirent *entry;
    char *hidden_files = getenv("HIDDEN");
    char *hidden_file;
    char *copy;

    while ((entry = orig_readdir(dirp))) {
        copy = strdup(hidden_files);
        hidden_file = strtok(copy, ":");

        while (hidden_file != NULL) {
            if (strcmp(entry->d_name, hidden_file) == 0) {
                free(copy);
                // Skip the hidden file
                return orig_readdir(dirp); 
            }
            hidden_file = strtok(NULL, ":");
        }

        free(copy);
        return entry;
    }

    return NULL;
}