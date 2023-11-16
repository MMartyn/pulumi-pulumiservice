# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TeamAccessTokenArgs', 'TeamAccessToken']

@pulumi.input_type
class TeamAccessTokenArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 organization_name: pulumi.Input[str],
                 team_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TeamAccessToken resource.
        :param pulumi.Input[str] name: The name for the token. This must be unique amongst all machine tokens within your organization.
        :param pulumi.Input[str] organization_name: The organization's name.
        :param pulumi.Input[str] team_name: The team name.
        :param pulumi.Input[str] description: Optional. Team description.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "organization_name", organization_name)
        pulumi.set(__self__, "team_name", team_name)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name for the token. This must be unique amongst all machine tokens within your organization.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> pulumi.Input[str]:
        """
        The organization's name.
        """
        return pulumi.get(self, "organization_name")

    @organization_name.setter
    def organization_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_name", value)

    @property
    @pulumi.getter(name="teamName")
    def team_name(self) -> pulumi.Input[str]:
        """
        The team name.
        """
        return pulumi.get(self, "team_name")

    @team_name.setter
    def team_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Team description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class TeamAccessToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None,
                 team_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Pulumi Cloud allows users to create access tokens scoped to team. Team access tokens is a resource to create them and assign them to a team

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. Team description.
        :param pulumi.Input[str] name: The name for the token. This must be unique amongst all machine tokens within your organization.
        :param pulumi.Input[str] organization_name: The organization's name.
        :param pulumi.Input[str] team_name: The team name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TeamAccessTokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Pulumi Cloud allows users to create access tokens scoped to team. Team access tokens is a resource to create them and assign them to a team

        :param str resource_name: The name of the resource.
        :param TeamAccessTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TeamAccessTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None,
                 team_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TeamAccessTokenArgs.__new__(TeamAccessTokenArgs)

            __props__.__dict__["description"] = description
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if organization_name is None and not opts.urn:
                raise TypeError("Missing required property 'organization_name'")
            __props__.__dict__["organization_name"] = organization_name
            if team_name is None and not opts.urn:
                raise TypeError("Missing required property 'team_name'")
            __props__.__dict__["team_name"] = team_name
            __props__.__dict__["value"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["value"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(TeamAccessToken, __self__).__init__(
            'pulumiservice:index:TeamAccessToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TeamAccessToken':
        """
        Get an existing TeamAccessToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TeamAccessTokenArgs.__new__(TeamAccessTokenArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization_name"] = None
        __props__.__dict__["team_name"] = None
        __props__.__dict__["value"] = None
        return TeamAccessToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. Description for the token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for the token. This must be unique amongst all machine tokens within your organization.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> pulumi.Output[str]:
        """
        The organization's name.
        """
        return pulumi.get(self, "organization_name")

    @property
    @pulumi.getter(name="teamName")
    def team_name(self) -> pulumi.Output[str]:
        """
        The team name.
        """
        return pulumi.get(self, "team_name")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The token's value.
        """
        return pulumi.get(self, "value")

