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
    static struct dirent *(*orig_readdir)(DIR *) = NULL;
    
    // Load the og readdir() if not yet loaded
    if (!orig_readdir) {
        orig_readdir = dlsym(RTLD_NEXT, "readdir");
    }

    struct dirent *entry;
    char *hidden_files = getenv("HIDDEN");
    char *hidden_file;
    char *copy;

    while ((entry = orig_readdir(dirp))) {
        //Make copy of hiddlen_files to avoid changing the og string
        copy = strdup(hidden_files);
        hidden_file = strtok(copy, ":");

        while (hidden_file != NULL) {
            if (strcmp(entry->d_name, hidden_file) == 0) {
                //Need to free because of strdup
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