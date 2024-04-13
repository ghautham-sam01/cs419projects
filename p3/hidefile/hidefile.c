#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>
#include <dirent.h>
#include <stdlib.h>

// Name: Ghautham Sambabu
// netID: gs878
// RUID: 201003148
// your code for readdir goes here

// Define the original readdir function type
typedef struct dirent *(*readdir_t)(DIR *);

// Define the HIDDEN environment variable
static const char *hidden_files[128] = {NULL};
static int num_hidden_files = 0;

// Function to get the value of the HIDDEN environment variable
static void get_hidden_files() {
    const char *hidden_env = getenv("HIDDEN");
    if (hidden_env) {
        char *hidden_copy = strdup(hidden_env);
        if (hidden_copy) {
            char *token = strtok(hidden_copy, ":");
            num_hidden_files = 0;
            while (token != NULL && num_hidden_files < 128) {
                hidden_files[num_hidden_files++] = token;
                token = strtok(NULL, ":");
            }
            free(hidden_copy);
        }
    }
}

// Implementation of the readdir function
struct dirent *readdir(DIR *dirp) {
    // Load the original readdir function
    readdir_t original_readdir = dlsym(RTLD_NEXT, "readdir");
    
    // If HIDDEN is not set or original_readdir is NULL, call original readdir
    if (num_hidden_files == 0 || !original_readdir) {
        return original_readdir(dirp);
    }
    
    struct dirent *entry;
    
    // Loop until we find a non-hidden file or reach the end of the directory
    while ((entry = original_readdir(dirp)) != NULL) {
        // Check if the current file matches any of the hidden file names
        int hidden = 0;
        for (int i = 0; i < num_hidden_files; ++i) {
            if (strcmp(entry->d_name, hidden_files[i]) == 0) {
                hidden = 1;
                break;
            }
        }
        if (hidden) {
            // Skip this entry
            continue;
        }
        
        // Return the non-hidden file entry
        return entry;
    }
    
    // If no non-hidden file found, return NULL
    return NULL;
}
