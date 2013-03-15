#!/usr/bin/python

import sys
import time
import os
from collections import namedtuple
import ctypes

class HFSplus:
    def __init__(self):
        self = self
        HFSPlusVolumeHeader = namedtuple(
                                                                                            "HFSPlusVolumeHeader", "field1 field2 field3")
        
    def volume_reader(self)
        # os.pread(fd, buffersize, offset)
        os.pread(fd, vheader, 1024)
        
        
        
#/* HFS Plus Volume Header - 512 bytes */
#/* Stored at sector #2 (3rd sector) and second-to-last sector. */
#struct HFSPlusVolumeHeader {
#   ctypes.u_int16_t    signature;      /* == kHFSPlusSigWord */
#   ctypes.u_int16_t    version;        /* == kHFSPlusVersion */
#   ctypes.u_int32_t    attributes;     /* volume attributes */
#   ctypes.u_int32_t    lastMountedVersion; /* implementation version which last mounted volume */
#   ctypes.u_int32_t    journalInfoBlock;   /* block addr of journal info (if volume is journaled, zero otherwise) */
#
#   ctypes.u_int32_t    createDate;     /* date and time of volume creation */
#   ctypes.u_int32_t    modifyDate;     /* date and time of last modification */
#   ctypes.u_int32_t    backupDate;     /* date and time of last backup */
#   ctypes.u_int32_t    checkedDate;        /* date and time of last disk check */
#
#   ctypes.u_int32_t    fileCount;      /* number of files in volume */
#   ctypes.u_int32_t    folderCount;        /* number of directories in volume */
#
#   ctypes.u_int32_t    blockSize;      /* size (in bytes) of allocation blocks */
#   ctypes.u_int32_t    totalBlocks;        /* number of allocation blocks in volume (includes this header and VBM*/
#   ctypes.u_int32_t    freeBlocks;     /* number of unused allocation blocks */
#
#   ctypes.u_int32_t    nextAllocation;     /* start of next allocation search */
#   ctypes.u_int32_t    rsrcClumpSize;      /* default resource fork clump size */
#   ctypes.u_int32_t    dataClumpSize;      /* default data fork clump size */
#   ctypes.u_int32_t    nextCatalogID;      /* next unused catalog node ID */
#
#   ctypes.u_int32_t    writeCount;     /* volume write count */
#   ctypes.u_int64_t    encodingsBitmap;    /* which encodings have been use  on this volume */
#
#   ctypes.u_int8_t     finderInfo[32];     /* information used by the Finder */
#
#   HFSPlusForkData  allocationFile;    /* allocation bitmap file */
#   HFSPlusForkData  extentsFile;       /* extents B-tree file */
#   HFSPlusForkData  catalogFile;       /* catalog B-tree file */
#   HFSPlusForkData  attributesFile;    /* extended attributes B-tree file */
#   HFSPlusForkData  startupFile;       /* boot file (secondary loader) */
#};
#typedef struct HFSPlusVolumeHeader HFSPlusVolumeHeader;
